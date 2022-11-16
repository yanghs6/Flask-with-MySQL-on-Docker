-- Create customUser
CREATE USER "customUser"@"172.%.%.%" IDENTIFIED BY "mysql";
CREATE USER "root2"@"%" IDENTIFIED BY "root2";

-- Grant customUser
GRANT ALL ON *.* TO "customUser"@"172.%.%.%";
GRANT ALL ON *.* TO "root2"@"%";
