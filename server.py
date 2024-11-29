import asyncio
import websockets
from analysis import AIAnalysisSystem

async def handler(websocket):
    analysis_system = AIAnalysisSystem()
    async for message in websocket:
        question, response = message.split('|')
        
        # Edge case handling
        edge_case_feedback = analysis_system.handle_edge_cases(response)
        if edge_case_feedback:
            await websocket.send(f"Feedback: {edge_case_feedback}")
            continue
        
        # Score and feedback
        score, feedback = analysis_system.score_response(question, response)
        await websocket.send(f"Score: {score} | Feedback: {feedback}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
