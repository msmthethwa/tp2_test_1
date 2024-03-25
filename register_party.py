"""Write a python function named “register_party” that takes a list of parties. 
Each party must be presented by key value pairs. The keys should be “party_name”, “reg_number”, “member_count”). 
The function should check if the new party has acceptable number of 
members for it to be registered as per the requirements narrated in the scenario."""

def register_party(parties, new_party):
    
    party_requirements = {'EFF':10003312, 'ANC':10003313, 'ASA':10003314, 'NFP': 10003315, 'IFP': 10003316,'MFT': 10003317}
     
    
    if new_party["party_name"] not in party_requirements:
        print("Part is not registerd!!!")
        if new_party["member_count"] <= 1000:
            print("Party can be registered. Member count does meet requirements for registration")
            parties.append(new_party)
        else:
            print("Party can not be registered. Member count does not meet requirements for registration.")
    else:
        print("Part is already registerd")

    


parties_list = [
    {"party_name": "Party A", "reg_number": 10003316, "member_count": 20532},
    {"party_name": "Party B", "reg_number": 10003317, "member_count": 10932}
]

last_registered_number = 10003318

new_party = new_party = {
    "party_name": "MK Party",
    "reg_number": last_registered_number + 1,
    "member_count": 5300
}
register_party(parties_list, new_party)
print(parties_list)

"""Implement a function called “update_voter_info” where each key is a voter_id and the 
value is another dictionary containing name, voting_district and has_voted. The function 
should update the voter’s information or add a vote if not already voted. Very important hint:
you should think of best practices for source code management and collaboration using git, 
for instances; is it a good practice to answer this question under the directories that are already 
existing or you should create a feature branch for development. From this question onwards 
you won’t be guided like you have been on questions prior to this. Always think best practices 
for software development as discussed in class. Create a new file, new directory, new feature 
branch where necessary"""

def update_voter_info(voters_dict, info):
    # Checking if the voter id  exists in the dict
    if info['voter_id'] in voters_dict:
        # Updating the existing voter's information
        voters_dict[info['voter_id']]['name'] = info['name']
        voters_dict[info['voter_id']]['voting_district'] = info['voting_district']
        
        # Adding the vote only if the user hasn't casted his/her vote yet
        if not voters_dict[info['voter_id']]['has_voted']:
            voters_dict[info['voter_id']]['has_voted'] = True
            voters_dict[info['voting_station']].append(info['voter_id'])
            
    else:
        # If the voter doesn't exist we add him/her with the provided information
        voters_dict[info['voter_id']] = {}
        voters_dict[info['voter_id']]['name'] = info['name']
        voters_dict['stations'].append(info['voting_station'])
        voters_dict[info['voter_id']]['voting_district'] = info['voting_district']
        voters_dict['total_voters'] += 1
    
# Creating an empty dictionary for storing all the voters information
all_voters = {'total_voters': 0, 'stations': []}

# Calling the function to add some  voters information
update_voter_info(all_voters, {'voter_id': '1', 'name': 'John Doe', 'voting_district': 'A', 'voting_station':'Station A'})

"""Using list comprehension and the filter function, write a piece of code that filters out all 
parties from a given list that have less than 1,000 members. Use ALL the parties that are on 
the ballot paper in Annexure A as your list elements, only capture their abbreviation as 
elements e.g. capture EFF on your list of elements instead of “Economic Freedom Fighters”
as it is displayed using EFF abbreviation on the ballot paper.""" 

parties = [{'abbreviation':'African National Congress', 'members':23546789},
           {'abbreviation':'Inkatha', 'members':12345678},
           {'abbreviation':'Nationalist MPU', 'members':987654321},
           {'abbreviation':'UDF', 'members':1001}]

filtered_parties = [party['abbreviation'] for party in parties if party['members'] >= 1000]
print(filtered_parties)


#Rewrite the list comprehension into a normal list data structure.
normal_list=list(filtered_parties)
print(normal_list)  
#Adding the voting stations information to the overall voters information
all_voters['stations'] = sorted(set(all_voters['stations'] + voters_dict['  stations']))

# Printing the final voters information 
print("Number of total voters: ", all_voters['total_voters'], "\n", "Voting Stations: ", end="")
for station in all_voters['stations']:
    print("\nStation: ", station, sep='')
    ids = ', '.join(map(str, voters_dict[station].keys()))
    print("Voters IDs: ", ids)

"""Write a python expression using a lambda function and the filter function to extract only 
those records where the voter is marked as registered ('registered': True). Assign the result 
to a variable named “registered_voters”."""
registered_voters = list(filter(lambda x : x['registered'], voters_dict.values()))
print ("\nRegistered Voters:\n",end="")
for v in registered_voters:
    print (f"ID: {v['id']}\tName: {v['name']}") 
    
#
