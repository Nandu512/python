is_logged_in=True
is_subscribed=False
user_credits=100
max_credits=200
min_credits=50
credits_valid=user_credits>=min_credits and user_credits<=max_credits and user_credits!=min_credits
bonous_eligible=is_subscribed or user_credits>min_credits
user_credits+=50
user_credits-=20
user_credits*=2
user_credits%=150
user_credits**=2
power_result=user_credits
full_acess=is_logged_in and is_subscribed
is_true_login=is_logged_in is True
acess_result=is_logged_in or is_subscribed
print('is logged is',is_logged_in)
print('is subscribed is', is_subscribed)
print('is credits valid is',credits_valid)
print('bonous eligible is',bonous_eligible)
print('user credits is:',user_credits)
print('power result',power_result)
print('full acess',full_acess)
print('is true login',is_true_login)
print('acess result',acess_result)