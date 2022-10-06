from .client import TransCovClient
from database.dto import TcDataDTO, TcLinkDTO
from database.insert import Insert

class BuildTrasnCovData:
    def __init__(self) -> None:
        self.insert_data = Insert()

    def create_data(self):
        tras_cov = TransCovClient()
        print("Geting Transparency in Coverage links...")
        links = tras_cov.get_coverage_links()
        if not links["success"]:
            return {"success": False, "error": "error in retrive links from transparency coverage"}
        index = 0
        blob_len = len(links["blobs"])
        for link in links["blobs"]:
            print(f"saving {index}/{blob_len}")
            index+=1
            if link["downloadUrl"].endswith("index.json"):
                json_result = tras_cov.get_json_file_from_link(link["downloadUrl"])
                if json_result["success"]:
                    self.save_result(link,json_result["data"] )
    
    def save_result(self, link, data):
        for report in data["reporting_structure"]:
            for report_plan in report["reporting_plans"]:

                plan_data = report_plan
                plan_data["in_network_files"] = report.get("in_network_files",[])
                plan_data["allowed_amount_file"] = report.get("allowed_amount_file",[])

                tc_link_dto = TcLinkDTO(link["name"],link["downloadUrl"])
                Tc_Data_dto = TcDataDTO(company_ein=report_plan["plan_id"],company_name=report_plan["plan_name"], data = str(plan_data))
                self.insert_data.insert_link_and_data(tc_link_dto, Tc_Data_dto)

    