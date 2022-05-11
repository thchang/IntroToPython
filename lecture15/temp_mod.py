FREEZING_POINT_F = 32
FREEZING_POINT_K = 273.15

def F_to_C(tempF):
    """ Convert temperature in degrees F -> degrees C.

    Args:
        tempF (float): The temperature in degrees F

    Returns:
        tempC (float): The temperature in degrees C

    """
    tempC = (tempF - FREEZING_POINT_F) * 5 / 9
    return tempC

def C_to_F(tempC):
    """ Convert temperature in degrees C -> degrees F.

    Args:
        tempC (float): The temperature in degrees C

    Returns:
        tempF (float): The temperature in degrees F

    """
    tempF = (tempC * 9 / 5) + FREEZING_POINT_F
    return tempF

def C_to_K(tempC):
    """ Convert temperature in degrees C -> Kelvins.

    Args:
        tempC (float): The temperature in degrees C

    Returns:
        tempK (float): The temperature in Kelvins

    """
    tempK = tempC + FREEZING_POINT_K
    return tempK
