import asyncio

from codeact.agent.codeact import CodeActAgent


async def main():
    agent = CodeActAgent()
    while True:
        try:
            prompt = input("\nEnter your prompt (or 'exit' to quit): ")
            if prompt.lower() == 'exit':
                print("Goodbye!")
                break
            print("\nProcessing your request...\n")
            await agent.run(prompt)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
