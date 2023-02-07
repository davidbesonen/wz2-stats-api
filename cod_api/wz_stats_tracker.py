from cod_api import API, platforms
import asyncio

# Path: cod_api/wz_stats_tracker.py
api = API()
api.login('MTU0Mzg2Njc0MjQwNjQ5NDA0MjoxNjc3MDA0OTUwNTkxOjI0YjEyYjMyN2JjMmQ1MDhkMDNiY2NiYzg2Njg0ZDk2')

# async
# in an async function
async def example():
    # login in with sso token
    await api.loginAsync('MTU0Mzg2Njc0MjQwNjQ5NDA0MjoxNjc3MDA0OTUwNTkxOjI0YjEyYjMyN2JjMmQ1MDhkMDNiY2NiYzg2Njg0ZDk2')

    # retrieving combat history
    profile = await api.Warzone2.fullDataAsync(platforms.Battlenet, "Magnumox#1645") # returns data of type dict

    # printing results to console
    print(profile)

asyncio.run(example())

# CALL THE example FUNCTION IN AN ASYNC ENVIRONMENT