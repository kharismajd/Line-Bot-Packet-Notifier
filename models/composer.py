from datetime import datetime
import time

class Composer:
    composed_data = {"shipment_status": None, "last_update": None, "records": []}

    def compose(self, kurir, data):
        if kurir == "JNE":
            self.__JNE(data)
        elif kurir == "J&T":
            self.__JNT(data)
        elif kurir == "AnterAja":
            self.__AnterAja(data)
        if kurir == "Sicepat":
            self.__SiCepat(data)
        elif kurir == "Tiki":
            self.__Tiki(data)
        elif kurir == "Ninja Xpress":
            self.__Ninja(data)
        if kurir == "POS Indonesia":
            self.__POS(data)
        elif kurir == "Wahana":
            self.__Wahana(data)
        elif kurir == "Lion Parcel":
            self.__Lion(data)
        elif kurir == "Shopee Xpress":
            self.__SPX(data)

    def __JNE(self, data):
        data_array = data.split('\n')

        self.composed_data = {"shipment_status": data_array[1], "last_update": None, "records": []}

        for i in range(12, len(data_array), 3):
            datetime_str = data_array[i - 2]

            if i == 12:
               self.composed_data["last_update"] = datetime_str

            self.composed_data["records"].append({"datetime": datetime_str, "status": data_array[i]})

    def __JNT(self, data):
        data_array = data.split('\n')

        self.composed_data = {"shipment_status": data_array[1], "last_update": None, "records": []}

        for i in range(6, len(data_array), 3):
            datetime_str = data_array[i - 2]

            if i == 6:
               self.composed_data["last_update"] = datetime_str

            self.composed_data["records"].append({"datetime": datetime_str, "status": data_array[i]})

    def __AnterAja(self, data):
        data_array = data.split('\n')

        self.composed_data = {"shipment_status": data_array[1], "last_update": None, "records": []}

        for i in range(5, len(data_array), 2):
            datetime_str = data_array[i - 1]

            if i == 5:
                self.composed_data["last_update"] = datetime_str

            self.composed_data["records"].append({"datetime": datetime_str, "status": data_array[i]})

    def __SiCepat(self, data):
        print("TODO: SiCepat")

    def __Tiki(self, data):
        print("TODO: TIKI")

    def __Ninja(self, data):
        print("TODO: Ninja")

    def __POS(self, data):
        print("TODO: POS")

    def __Wahana(self, data):
        print("TODO: Wahana")

    def __Lion(self, data):
        print("TODO: Lion")

    def __SPX(self, data):
        print("TODO: Shopee Xpress")