Exception in thread "main" com.fasterxml.jackson.databind.exc.UnrecognizedPropertyException: Unrecognized field "CountryDialingCode" (class Models.ContactProvided), not marked as ignorable (3 known properties: "EmailAddressValue", "Label", "Phone"])
 at [Source: (File); line: 142, column: 62] (through reference chain: Models.OrderCreateRQ["Query"]->Models.Query["DataLists"]->Models.DataLists["ContactList"]->java.util.ArrayList[0]->Models.ContactInformation["ContactProvided"]->java.util.ArrayList[0]->Models.ContactProvided["CountryDialingCode"])


public class ContactInformation {
    public String ContactID;
    public String ContactType;
    public List<ContactProvided> ContactProvided;

}
class ContactProvided{
    public String EmailAddressValue;
    public Phone Phone;
    public String Label;
}
class Phone{
    public String Label;
    public String CountryDialingCode;
    public String AreaCode;
    public String PhoneNumber;

}
