import paramiko
import os

paramikos_world = '/home/student/mycode/paramikosftp'  # CHANGE
test_environment = '/home/bender/testdir/'             # CHANGE


def movethemfiles(sftp):
                        # list the contents of /home/student/mycode/paramikosftp on BCHD
    givemedemfiles = os.listdir(paramikos_world)
   # list of files on BCHD folder
    return givemedemfiles

t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)


for secret_files in movethemfiles(sftp):  # Missing colon at the end of this line
    paramikos_filepath = paramikos_world + '/' + secret_files
    # ^ absolute path to each file

    test_filepath = test_environment + '/' + secret_files
    # ^ new absolute path to the file once copied to bender

    sftp.put(paramikos_filepath, test_filepath)  # Typo: 'parmikos_filepath' should be 'paramikos_filepath'

    print(f"Downloaded {secret_files} to {test_filepath}")

