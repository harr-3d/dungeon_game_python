class ExperienceLevel:
    """Defines level by total experience points"""

    def __init__(self):
        self.current_level = 1
        self.levels = {1: 1, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500,
                       7: 600, 8: 700, 9: 800, 10: 900}
    
    def level_check(self, current_xp_points):
        """Return the player's current level based on xp"""
        for level, xp_needed in self.levels.items():
            if current_xp_points > xp_needed:
                self.current_level = level

        return self.current_level