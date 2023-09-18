import os
import sys

# Path to the main.py script
main_script_path = '/home/ehsan/PycharmProjects/DemoTFTAI_LIVE_OR_NOT/main.py'  # Replace with your actual path

# Verify that the main.py script exists
if not os.path.isfile(main_script_path):
    print(f"Error: The file '{main_script_path}' does not exist.")
    sys.exit(1)

# Create a cron job schedule string that run this will at 5 mints
cron_schedule = f'*/5 * * * * /usr/bin/python3 {main_script_path}'

# Add the cron job
try:
    # Save current user's crontab to a temporary file
    os.system('crontab -l > mycron')

    # Append the new cron job schedule to the temporary file
    with open('mycron', 'a') as f:
        f.write(f'{cron_schedule}\n')

    # Install the new crontab from the temporary file
    os.system('crontab mycron')

    print("Cron job added successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Clean up the temporary file
os.remove('mycron')
