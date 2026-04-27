import json

class ReflectionTree:
    def __init__(self, data_path):
        with open(data_path, 'r') as f:
            self.nodes = json.load(f)
            
    def run(self):
        current_node_id = "start"
        print("--- Daily Reflection Tree ---")
        
        while True:
            node = self.nodes.get(current_node_id)
            print(f"\n[?] {node['question']}")
            
            if not node['options']:
                print("\nReflection Complete. Thank you for being honest with yourself.")
                break
                
            options = list(node['options'].keys())
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
                
            try:
                choice = int(input("Select an option (number): "))
                selected_key = options[choice - 1]
                current_node_id = node['options'][selected_key]
            except (ValueError, IndexError):
                print("Invalid input. Please focus and try again.")