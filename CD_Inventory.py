#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Tian, 3/14/20, added Dataprocessor)
# Tian Xie, 2020-March-13, created file.
# Tian Xie, 2020-March-14, cleaned up code and updated docstrings.
#------------------------------------------#
import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []

class CD(object):

    """Stores data about a CD:
    
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        None
    """
    # -- Initializer / Instance Attributes -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = int(value)

    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        self.__title = str(value)

    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = str(value)

# -- PROCESSING -- #

class DataProcessor:
    """Adding/Deleting Inventory"""
    @staticmethod
    # adding class instance to lst_cdObj
    def add_inventory(cd_id, cd_title, cd_artist, lst_cdObj):
        added_cdObj = CD(cd_id, cd_title, cd_artist)
        lst_cdObj.append(added_cdObj)
        return lst_cdObj

    @staticmethod
    def del_inventory(lst_cdObj):
        intIDDel = input('Which ID would you like to delete? Please make sure you enter a number ').strip()
        while True:
            try:
                int(intIDDel)
                break
            except ValueError:
                intIDDel = input('Error: ID must be an integer. Enter ID: ').strip()
        # 3.5.2 search thru lstOfCDObjects and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in lst_cdObj:
            intRowNr += 1
            if row.cd_id == intIDDel:
                del lst_cdObj[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return lst_cdObj

class FileIO:
    """Processes data to and from file:

    properties:
        None

    methods:
        save_inventory(file_name, table): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def save_inventory(file_name, lst_cdObj):
        """Function to save binary data to the file identified by file_name into a 2D lstOfCDObjects

       Args:
           file_name (string): name of file used to read the data from
           lst_cdObj: 2D data structure (list of objects) that holds the data during runtime

       Returns:
           None.
       """
        with open(file_name, 'wb') as objFile:
            pickle.dump(lst_cdObj, objFile)

    @staticmethod
    def load_inventory(file_name, lst_cdObj):
        """Function to manage binary data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D lstOfCDObjects
        (list of dicts) lst_cdObj one line in the file represents one dictionary row in lst_cdObj.

        Args:
            file_name (string): name of file used to read the data from
            lst_cdObj: 2D data structure (list of objects) that holds the data during runtime

        Returns:
            lst_cdObj.
        """
        # Making sure the program won't crash if file doesn't exist.

        try:
            with open(file_name, 'rb') as objFile:
                lst_cdObj = pickle.load(objFile)
        except FileNotFoundError:
            print("Warning: There's no file in the directory.")
        return lst_cdObj


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lst_cdObj):
        """Displays current inventory table


        Args:
            lst_cdObj: 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_cdObj:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')

    @staticmethod
    def get_userinput():
        """Displays guidance for user input

        Args:
            None

        Returns:
            intID, strTitle, strArtist

        """
        # Ask user for new ID, CD Title and Artist
        intID = input('Enter ID: ').strip()
        while True:
            try:
                int(intID)
                break
            except ValueError:
                intID = input('Error: ID must be a number. Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, strArtist


# 1. When program starts, read in the currently saved Inventory
lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        IO.show_inventory(lstOfCDObjects)
        intID, strTitle, strArtist = IO.get_userinput()
        lstOfCDObjects = DataProcessor.add_inventory(intID, strTitle, strArtist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        IO.show_inventory(lstOfCDObjects)
        lstOfCDObjects = DataProcessor.del_inventory(lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print("CD inventory file has been saved!")
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
