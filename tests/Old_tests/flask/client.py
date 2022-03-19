import requests


if __name__ == '__main__':
    req = requests.get('http://127.0.0.1:8000/list_pc/')
    print(req.json()["first"])

    print(requests.post('http://127.0.0.1:8000/calc/',data=({'a':5,'b':6,'c':90})).text)

    my_pos = (0,0)

    name = input('Whats name? :')
    print(requests.post('http://127.0.0.1:8000/newuser/',data={'name':name,'pos':my_pos}))


    while True:
        get = input(":")
        print(f"my pos now {my_pos}")
        match get:
            case 'mypos':
                my_pos = requests.post('http://127.0.0.1:8000/mypos/',data={'name':name})
            case 'newpos':
                x = int(input('x : '))
                y = int(input('y : '))
                requests.post('http://127.0.0.1:8000/newpos/',data={'name':name,'x':x,'y':y})