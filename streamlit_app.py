
from pprint import pprint

import inquirer


questions = [
  inquirer.List('nodename',
                message="What nodename would you be using do you need?",
                choices=["gpu-eu-w2a", "gpu-eu-w2b", "pool-infra", "pool-micro-services-cpu", "pool-pulsar"],
            ),
]
answers = inquirer.prompt(questions)
pprint(answers["choices"])




numberofnodes = input ("how many nodes are needed?")

questions = [
  inquirer.List('machinetype',
                message="What machinetype would you be using do you need?",
                choices=["n1-standard-4", "n2-standard-4", "n2-standard-16"],
            ),
]
answers = inquirer.prompt(questions)
print (answers["machinetype"])



pphinstance  = input ("how many pph/instance?")

minuser  = input ("how many min users?")

maxuser  = input ("how many max users?")


guessmax  = input ("guess how many max users?")

minuserpernode  = input ("minuser / float(numberofnodes)")


users  = input ("guess how many max users?")



questions = [
  inquirer.List('services',
                message="What services would you be using?",
                choices=["polyp-det", "ms-all", "websocket, webserver", "freeze, image storage, prediction storage", "pulsar"],
            ),
]
answers = inquirer.prompt(questions)
print (answers["machinetype"])



users  = input ("guess how many max users?")

runtimedayinhrs  = input ("what is the runtime daily in hours?")

daysperweek  = input ("how many days in a week?")

procedurelength  = input ("procedure length in hrs?")







print(numberofnodes)





nodeneeded = {
    print (answers["nodename"])
(users / minuserpernode(100))

}

costpermonth = {
    print (answers["costpermonth"])
           (nodeneeded * runtimedayinhrs * daysperweek * 4.345 * pphinstance)


}
