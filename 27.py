facebook = True
twitter = False
instagram = True

if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("A person can be a good influencer!")
else:
    print("A person cannot be a good influencer.")