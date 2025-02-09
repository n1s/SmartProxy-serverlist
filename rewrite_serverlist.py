import os

# Define the $user and $pass variables
user = os.getenv("VPN_USER", "default_user")
password = os.getenv("VPN_PASS", "default_password")
hostlist = os.getenv("HOSTLIST", "input.txt")

# Open the input file for reading and the output file for writing
with open(hostlist, "r") as input_file, open("serverlist.txt", "w") as output_file:
    # Loop over each line in the input file
    for line in input_file:
        # Remove any leading/trailing whitespace
        line = line.strip()

        if line.startswith(('[', '#')):
            output_file.write(line + "\n")
            continue  # Skip to the next line


        # Extract the domain part (before the first dot)
        domain = line.split('.')[0]

        # Replace placeholders [$COUNTRY], [$user], and [$pass] with actual values
        updated_line = "{0}:89 [HTTPS] [{1}] [{2}] [{3}]".format(
              line,
              domain,  # {1} - Country code
              user,    # {2} - Username
              password # {3} - Password
        )

        # Write the updated line to the output file
        output_file.write(updated_line + "\n")
