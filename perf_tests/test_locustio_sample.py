from locust import HttpLocust, TaskSet, task
import uuid

class GetOfferTasks(TaskSet):
    def generate_get_offer_request(self):
        email = uuid.uuid4()
        payload ="""
        <OfferRequestDto>
            <SubProgramId>2</SubProgramId>
            <FirstName>MONISE</FirstName>
            <MiddleInitial></MiddleInitial>
            <LastName>KELLY</LastName>
            <Suffix/>
            <EmailAddress>%s@c1.dev</EmailAddress>
            <DateOfBirth>01/01/1963</DateOfBirth>
            <Street>14511 STAR CROSS TR</Street>
            <City>HELOTES</City>
            <State>TX</State>
            <Zipcode>78023</Zipcode>
            <LoanAmount>5000</LoanAmount>
            <LoanPurposeId>1</LoanPurposeId>
            <YearlyIncome>120000</YearlyIncome>
            <YearlyIncomeVerifiable>TRUE</YearlyIncomeVerifiable>
            <EmploymentStatusId>7</EmploymentStatusId>
            <SelfReportedCreditScore>728</SelfReportedCreditScore>
            <HomePhoneAreaCode>415</HomePhoneAreaCode>
            <HomePhoneNumber>593-5450</HomePhoneNumber>
            <MobilePhoneAreaCode>925</MobilePhoneAreaCode>
            <MobilePhoneNumber>212-5555</MobilePhoneNumber>
            <WorkPhoneAreaCode>415</WorkPhoneAreaCode>
            <WorkPhoneNumber>226-2960</WorkPhoneNumber>
            <SSN>666302683</SSN>
            <EmployerName>Test</EmployerName>
            <EmployerPhoneAreaCode>415</EmployerPhoneAreaCode>
            <EmployerPhoneNumber>593-5451</EmployerPhoneNumber>
            <EmploymentMonth>2</EmploymentMonth>
            <EmploymentYear>2000</EmploymentYear>
            <OccupationId>2</OccupationId>
            <BankName>Test Bank</BankName>
            <FirstAccountHolderName>MONISE</FirstAccountHolderName>
            <AccountNumber>123456789</AccountNumber>
            <RoutingNumber>113024520</RoutingNumber>
        </OfferRequestDto>
        """ % email
        return payload

    @task
    def get_offer_dx(self):
        headers ={"Content-Type":"application/xml","Authorization":"Basic Q3JlZGl0S2FybWEyOkNBQjVDQTExLTYzNDI="}
        response = self.client.post("/GetOffers",headers=headers,data=self.generate_get_offer_request())
        print response.json()


class WebsiteUser(HttpLocust):
    host = "http://services.stg2.circleone.com/DXReferral/API"
    task_set = GetOfferTasks
    min_wait = 5000
    max_wait = 15000
