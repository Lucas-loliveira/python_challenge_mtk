
class TcLinkDTO:
    def __init__(self, name, download_link) -> None:
        self.name = name
        self.download_link = download_link

class TcDataDTO:
    def __init__(self,company_ein,company_name, data, link_id=None) -> None:
        self.company_ein = company_ein
        self.company_name = company_name
        self.data = data
        self.link_id = link_id
