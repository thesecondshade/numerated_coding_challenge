import datetime
import requests
import sys


def main():
    """
        This function collects the route id from the get_route() function, the
        direction id from the get_direction() function, and the stop id from
        the get_stop function. It takes this information and calls the
        get_prediction() function to predict the next three departure times.
    """
    route_id = get_route()
    direction_id = get_direction(route_id)
    stop_id = get_stop(route_id, direction_id)

    get_prediction(stop_id, direction_id, route_id)



def get_route():
    """
        This function calls the MBTA api in order to offer the user a complete
        list of routes and allow the user to choose which route they plan to
        travel on. After identifying the correct route, the route id is returned.

    """


    URL = 'https://api-v3.mbta.com/routes'
    resp = requests.get(URL)
    if resp.status_code != 200:
        print('Something has gone wrong with the MBTA website - check back later!')
        exit()
    else:
        data = resp.json()['data']
        route_list = {}
        print('\n Route Options:')
        for route in data:
            if route['attributes']['type'] < 2:
                print(route['attributes']['long_name'])
                route_list[route['attributes']['long_name']] = route['id']

        # Using a while loop to authenticate the user's input
        valid = False
        while valid == False:
            route = input('\n Which route are you travelling on today? \n')
            if route in route_list:
                route_id = route_list[route]
                valid = True
            else:
                print('This is not a valid route, please try again! \n')

        return route_id

def get_direction(route_id):
    """
        This function offers the user a list of direction options that are
        relevant to the route they chose. It also determines the direction id
        by it's index in the direction_names list in the api.
    """

    URL = f'https://api-v3.mbta.com/routes/{route_id}'
    resp = requests.get(URL)
    
    if resp.status_code != 200:
        print('Something has gone wrong with the MBTA website - check back later!')
        exit()
    else:
        data = resp.json()['data']
        print('\n Direction Options:')
        direction_list = {}
        i=0
        for name in data['attributes']['direction_names']:
            print(name)
            direction_list[name]=i
            i+=1

        # Using a while loop to authenticate the user's input
        valid = False
        while valid == False:
            direction = input('\n Which direction are you travelling in today? \n')
            if direction in direction_list:
                valid = True
            else:
                print('This is not a valid direction, please try again! \n')
        return direction_list[direction]



def get_stop(route_id, direction):
    """
        This function offers the user a complete list of stops based on the
        route and direction they have selected so far. It then returns the
        relevant stop id.
    """

    URL = f'https://api-v3.mbta.com/stops/?filter[route]={route_id}&[direction_id]={direction}'
    resp = requests.get(URL)
    if resp.status_code != 200:
        print('Something has gone wrong with the MBTA website - check back later!')
        exit()
    else:
        data = resp.json()['data']
        print('\n Stop Options: ')
        stop_list = {}
        for stop in data:
            print(stop['attributes']['name'])
            stop_list[stop['attributes']['name']]=stop['id']

        # Using a while loop to authenticate the user's input
        valid = False
        while valid == False:
            stop = input('\n Which stop are you departing from? \n')
            if stop in stop_list:
                stop_id = stop_list[stop]
                valid = True
            else:
                print('This is not a valid stop, please try again! \n')
        return stop_id


def get_prediction(stop_id, direction_id, route_id):
    """
        This function calculates the next three departure times based on the
        route, stop and direction chosen by the user. It them prints them to
        the user.
    """
    current_time = datetime.datetime.now()
    min_time = current_time.strftime("%H:%M")

    URL = f'https://api-v3.mbta.com/schedules?filter[stop]={stop_id}&filter[min_time]={min_time}&sort=time'
    resp = requests.get(URL)
    if resp.status_code != 200:
        print('Something has gone wrong with the MBTA website - check back later!')
        exit()
    else:
        data = resp.json()['data']
        time_list = []
        for x in data:
            if x['attributes']['direction_id']==direction_id and x['relationships']['route']['data']['id'] == route_id:
                if x['attributes']['arrival_time']==None:
                    time = x['attributes']['departure_time']
                    time_list.append(time[time.index('T')+1:time.index('T')+6])
                elif x['attributes']['departure_time']==None:
                    time = x['attributes']['arrival_time']
                    time_list.append(time[time.index('T')+1:time.index('T')+6])
                else:
                    time = x['attributes']['departure_time']
                    time_list.append(time[time.index('T')+1:time.index('T')+6])
        if time_list ==[]:
            print('There are no departures from that stop for the rest of the day.')
        else:
            print('\n The next departures from that stop are: \n')
            i = 0
            while i<3:
                print(time_list[i]+'\n')
                i+=1
    


if __name__ == '__main__':
    '''
        Entry point
    '''
    main()
