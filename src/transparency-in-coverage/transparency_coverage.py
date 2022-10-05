from client import TransCovClient

class BuildTrasnCovData:
    def __init__(self) -> None:
        pass

    def crete_data(self):
        tras_cov = TransCovClient()

        links = tras_cov.get_coverage_links()
        if not links["success"]:
            return {"success": False, "error": "error in retrive links from transparency coverage"}
        breakpoint()
        for link in links["blobs"]:
            if link["downloadUrl"].endswith("index.json"):
                data = tras_cov.get_json_file(link["downloadUrl"])
    
    def save_result():
        pass


t = BuildTrasnCovData()
t.crete_data()
    