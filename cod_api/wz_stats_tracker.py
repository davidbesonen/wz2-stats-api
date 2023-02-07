from cod_api import 
import asyncio

# Path: cod_api/wz_stats_tracker.py
api = API()
api.login('MTU0Mzg2Njc0MjQwNjQ5NDA0MjoxNjc3MDA0OTUwNTkxOjI0YjEyYjMyN2JjMmQ1MDhkMDNiY2NiYzg2Njg0ZDk2')

# retrieving combat history
profile = api.Warzone.fullData(platforms.Battlenet, "Username#1234") # returns data of type dict

# printing results to console
print(profile)

## async
# in an async function
async def example():
    # login in with sso token
    await api.loginAsync('your_sso_token')

    # retrieving combat history
    profile = await api.Warzone.fullDataAsync(platforms.Battlenet, "Username#1234") # returns data of type dict

    # printing results to console
    print(profile)

# CALL THE example FUNCTION IN AN ASYNC ENVIRONMENT