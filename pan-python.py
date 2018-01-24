import os
import sys
import time
import netmiko

select_command_list = []
select_destination_list = []


welcome_screen = """\


\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
                     __________________________  
            (__)    /                          |
            (oo)   / Welcome to PanAutonoma-v1 |
     /-------\/  --\ Service Owner: Mike Zipp  |
    / |     ||      \__________________________|
   *  ||----||                 
      ~~    ~~    
\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\// 
"""




def SENDCOMMANDAWS(device):
   print "Connecting to %s" % (device)
   net_connect = netmiko.ConnectHandler(**device)
   output = net_connect.find_prompt()
   print output
   for command in select_command_list:
      print "Sending command %s" % (command)
      output = net_connect.send_command_expect(command)
      print(output)
   time.sleep(4)
   output = net_connect.find_prompt()
   print(output)
   net_connect.disconnect()

def SENDCOMMANDENT(device):
   print "Connecting to %s" % (device)
   net_connect = netmiko.ConnectHandler(**device)
   output = net_connect.find_prompt()
   print output
   for command in select_command_list:
      print "Sending command %s" % (command)
      output = net_connect.send_command_expect(command)
      print(output)
   net_connect.disconnect()





def CONFIGUREAWS():
   type = "VM"
   SELECT_COMMANDS(type)
   SELECT_DESTINATIONS(type)
   username = raw_input("\nENTER USERNAME\n>")
   userpass = raw_input("\nENTER PASSWORD\n>")
   for ip in select_destination_list:
      device={
      'device_type':'paloalto_panos',
      'ip':ip,
      'username':username,
      'password':userpass,
      'port':22
      }
      print device
      commitconfirm = raw_input("ENTER Y TO CONFIRM\n>")
      if commitconfirm == "Y":
         SENDCOMMANDAWS(device)

def CONFIGUREENT():
   type = "ENTERPRISE"
   SELECT_COMMANDS(type)
   SELECT_DESTINATIONS(type)
   username = raw_input("\nENTER USERNAME\n>")
   userpass = raw_input("\nENTER PASSWORD\n>")
   for ip in select_destination_list:
      device={
      'device_type':'paloalto_panos',
      'ip':ip,
      'username':username,
      'password':userpass,
      'port':22
      }
      print device
      commitconfirm = raw_input("ENTER Y TO CONFIRM\n>")
      if commitconfirm == "Y":
         SENDCOMMANDENT(device)




def SELECT_COMMANDS(type):
   print "\n Enter %s COMMANDS below" % (type)
   select_command = raw_input("Input one command per line, end with an extra newline: ")
   while select_command is not "":
         select_command_list.append(select_command)
         select_command = raw_input("Input one command per line, end with an extra newline: ")
   print "SELECTED COMMANDS: %s" % (select_command_list)


def SELECT_DESTINATIONS(type):
   print "\n Enter %s DESTINATION IP below" % (type)
   select_destination = raw_input("Input one command per line, end with an extra newline: ")
   while select_destination is not "":
         select_destination_list.append(select_destination)
         select_destination = raw_input("Input one command per line, end with an extra newline: ")
   print "SELECTED DESTINATIONS: %s" % (select_destination_list)




###########
#MAIN MENU#
###########
def main():
   print welcome_screen
   userselect = raw_input ("\nEnter the number corresponding to your selection below:\n\n1 - Send command(s) to VM destinations\n2 - Send command(s) to ENT destinations\n3 - Exit program\n\n>")

   if userselect == "1":
      CONFIGUREAWS()
      sys.exit()

   if userselect == "2":
      CONFIGUREENT()
      sys.exit()


   if userselect == "3":
      print goodbye_screen
      print "Exiting program. Goodbye"
      sys.exit()

   else:
      print "Invalid Selection"

main()
