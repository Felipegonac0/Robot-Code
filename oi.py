import wpilib
from state import state

def setup_for_robot (robot):
	
    robot.sensor_1 = wpilib.DigitalInput(1)
    robot.sensor_2 = wpilib.DigitalInput(2)
    robot.sensor_3 = wpilib.DigitalInput(3)
    robot.sensor_4 = wpilib.DigitalInput(4)
    robot.sensor_5 = wpilib.DigitalInput(5)
	

def read_input ():
	stick = wpilib.Joystick(1)
	y_button = stick.getRawButton(3)
	state["button_y_on"] = y_button
	a_button = stick.getRawButton(1)
	state["line_follow"] = y_button



"""

NUBE -> Velcrolastic

	SUBIR LIFT (dos motores para arriba)
	BAJAR LIFT (dos motores para abajo)

	EMPUJAR HATCH (activar / desactivar pistones)

ARIS -> Montugarra
		
	SUBIR LIFT (dos motores para arriba)
	BAJAR LIFT (dos motores para abajo)

	TOMAR / SOLTAR HATCH (activar / desactivar pistones)

FELIPE -> Linefollow

	6 sensores
	si Y está presionado
		Mueve el chasis en base a lo que leas de los sensores

IsmA -> Chasis con mecanums
	
	ya sabes

RENATA -> IsmaFeeder

	subir / bajar el coso (1 motor arriba / abajo)
	take cargo, drop cargo (1 motor arriba / abajo)


"""