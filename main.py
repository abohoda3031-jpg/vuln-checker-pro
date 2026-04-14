import modules # Assuming 'modules' is the directory or collection of modules in the project

def main():
    # Initialize all modules
    try:
        modules.initialize_all()
        print("All modules initialized successfully.")
    except Exception as e:
        print(f"Error initializing modules: {e}")

    # Display system status
    try:
        system_status = modules.get_system_status()
        print("System Status:")
        print(system_status)
    except Exception as e:
        print(f"Error retrieving system status: {e}")

if __name__ == '__main__':
    main()