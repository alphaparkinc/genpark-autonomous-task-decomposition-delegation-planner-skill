from client import AutonomousTaskDecompositionDelegationPlannerClient

def main():
    client = AutonomousTaskDecompositionDelegationPlannerClient()
    agents = ["ResearchAgent", "CoderAgent", "QAAgent"]
    res = client.decompose_and_plan("Build and test Stripe payment integration", agents)
    print(f"Parallel: {res['parallel_executable']}")
    print(f"Est Duration: {res['estimated_duration_seconds']}s")
    print("Execution Plan:")
    for s in res["execution_graph_steps"]:
        print(f"  Step {s['step']}: {s['task']} -> {s['agent']}")

if __name__ == "__main__":
    main()
