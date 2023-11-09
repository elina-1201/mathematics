# Console application

This application is a helping tool for solving equations by using applied mathematics with following methods:

- Bisection method
- Regula falsi
- Newton–Raphson method
- Modified Newton Raphson method
- Secant method

The program is written for a college assignment. Its purpose is to eliminate errors while solving equations manually as well as being able to check the final results.

 <hr/>
For building this console app, some requirements are needed:

- [python3](https://www.python.org/downloads/)
- [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
- [tabulate](https://pypi.org/project/tabulate/)
- [pick](https://pypi.org/project/pick/)
- [simpy](https://pypi.org/project/simpy/)

The last three libraries can be installed via requirements.txt in the project:

```
pip install -r requirements.txt
```

<hr/>

_Starting the program with `cmd` from `src` folder:_

    python main.py

\
_The example of an input after picking the second equation and the first method:_

    -3
    6
    2
    3

the following output:\
![output](./images/output.jpg)

<hr>

### How to write the exponent:

\
![input](./images/input-exponent.jpg)

<br>
by writing the exponent have in mind that it it will be in the following format:

| console input | interpretation |
| ------------- | -------------- |
| -3            | 10^(-3)        |
| 4             | 10^4           |
| -6            | 10^(-6)        |

<br/>

### Note

There are no exception handlers, so have that in mind while using this app, if the console just closes without any alert, that probably means there was some problem with the inputs. In case it happens, running the app from `cmd` will make it possible to see the error that occured.
