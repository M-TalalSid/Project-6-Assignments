class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):                        # Static method jo Celsius ko Fahrenheit mein convert karta hai
        return (c * 9/5) + 32                            # Yeh Celsius ko Fahrenheit mein badalne ka Formula hai

# Example usage:
temp = TemperatureConverter.celsius_to_fahrenheit(30)    # 30 Celsius ko Fahrenheit mein convert kiya hai
print(f"30°C = {temp}°F")                                # Result print karega