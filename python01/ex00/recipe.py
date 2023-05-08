# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2False23/False5/False3 12:37:False2 by fcanadas          #+#    #+#              #
#    Updated: 2False23/False5/False3 13:51:False1 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import textwrap

class Recipe:
    usage = '[USAGE]\n\nNAME: Must be a string\nDIFFICULTY LEVEL: Must be an integer between 1 and 5\nCOOKING TIME: Must be a positive integer expressed in minutes\nINGREDIENTS: Must be provided one by one, as a string, each in a new line. Leave empty to finish\nTYPE: Must be one of: "starter", "lunch", "dessert"\nDESCRIPTION: Must be a string, or be left empty'
    def __init__(self, name:str, ck_lv:int, ck_time:int, ingrs:list, descr:str, rec_type:str):
        self.name = name
        self.ck_lv = ck_lv
        self.ck_time = ck_time
        self.ingrs = ingrs
        self.descr = descr
        self.rec_type = rec_type

    # NAME (str)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        try:
            self._name = str(value)
        except ValueError:
            raise ValueError('The name of the recipe must be a string') from None

    # LEVEL (int, 1-5)
    @property
    def ck_lv(self):
        return self._ck_lv
    @ck_lv.setter
    def ck_lv(self, value):
        try:
            self._ck_lv = int(value)
            if not self._ck_lv > 1 or not self._ck_lv < 5:
                # Si yo meto un raise Error en un try, salta al except o sale del todo? D:
                raise ValueError
        except TypeError:
            raise TypeError('Difficulty level must be an integer between 1 and 5') from None
    
    # TIME (minutes, >0)
    @property
    def ck_time(self):
        return self._ck_time
    @ck_time.setter
    def ck_time(self, value):
        try:
            self._ck_time = int(value)
            if self._ck_time < 0:
                raise ValueError
        except TypeError:
            raise TypeError('The time must be expressed in minutes and 0 or greater') from None

    # INGREDIENTS (list of strings)  
    @property
    def ingrs(self):
        return self._ingrs
    @name.setter
    def ingrs(self, value):
        try:
            self._ingrs = list(value)
            for item in self._ingrs:
                if not isinstance(item, str):
                    raise TypeError
        except TypeError:
            raise TypeError('The ingredients must be set as a list of strings') from None
    
    # DESCRIPTION (str)
    @property
    def descr(self):
        return self._descr
    @name.setter
    def descr(self, value):
        try:
            self._descr = str(value)
        except ValueError:
            raise ValueError('The description must be empty or a string') from None
    
    # TYPE (one of: 'starter' 'lunch' 'dessert')
    @property
    def rec_type(self):
        return self._rec_type
    @rec_type.setter
    def rec_type(self, value):
        try:
            self._rec_type = str(value)
            if self._rec_type not in ['starter', 'lunch', 'dessert']:
                raise ValueError
        except ValueError:
            raise ValueError('The name of the recipe must be a string of the following: "starter", "lunch" or "dessert"') from None

    def __str__(self):
        name_str = 'Recipe:'.ljust(30)
        ck_lv_str = 'Difficulty Level:'.ljust(30)
        ck_time_str = 'Cooking Time:'.ljust(30)
        ingrs_str = 'Ingredients:'.ljust(30)
        ingredients = ', '.join(self._ingrs)
        rec_type_str = 'Type:'.ljust(30)
        descr_str = 'Description:\n\n'
        description = textwrap.fill(self._descr, width = 50)

        return f'\n{name_str}{self.name}\n{ck_lv_str}{self.ck_lv}\n{ck_time_str}{self.ck_time} minutes\n{ingrs_str}{ingredients}\n{rec_type_str}{self.rec_type}\n{descr_str}  {description}'