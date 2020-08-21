    def sort(self):
        """
        Sort the robot's list.
        """
        ### Upon initiation, these are the robot's stats
        ### it is at position 0
        ### it is not holding anything
        ### the light is off

        # so to properly sort
        # 1 pick up the first item
        self.item_pickup()
        # 2 turn the item light on while holding item
        self.set_light_on()
        # 3 do a comparison and move forward until the end of list
        while self.can_move_right:
        # 4 if comparison returns 1
            if self.compare_item() == 1:
        # 5 do a swap item
                self.swap_item()
        # 6 move to the right
            self.move_right
        # 7 repeat 3-6 until can move right returns false
        # 8 while can move left, move left
        while self.can_move_left:
            self.move_left
        # repeat 3 - 8 until holding max item  
        # drop max item at the end
        if self.check_max == True:
            self.drop_max
        else:
            self.sweep_right

              def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.

        """

                if self._item == self._list[-1]:
            return self._list
        if self._item == None:
            if self.light_is_on:
                return self._list
            else:
                self.item_pickup()
                self.set_light_on()


        #At the beginning, pick up the first item, turn the light on

        while self.can_move_right():
            if self.compare_item() == 1:
                self.move_right()
                self.swap_item()
            elif self.compare_item() == 0:
                self.move_right()
        
        # Make sure we do full sweeps
        if self.at_end:
            self.move_left()
            if self.compare_item() == -1:
                self.item_drop()
                self.move_right()
                self.item_pickup()
            while self.can_move_left():
                self.move_left()
        self.sort()