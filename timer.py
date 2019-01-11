        



        if state["is_running_auto"]:
            state["auto_timer"] += 1

            if state["auto_timer"] <= 50:
                self.eguzki_motor.set(-1)
            elif state["auto_timer"] <= 100:
                self.eguzki_motor.set(-0.5)
            else:
                self.eguzki_motor.set(1)
        else:
            state["auto_timer"] = 0
            self.eguzki_motor.set(0)