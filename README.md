<OrderCreateRQ Version="17.2" PrimaryLangID="EN" AltLangID="EN" xmlns="http://www.iata.org/IATA/EDIST/2017.2">
      <Document>
        <Name>BA</Name>
      </Document>
      <Party>
        <Sender>
          <TravelAgencySender>
            <Contacts>
              <!--Contact is optional for Non-IATA-->
              <Contact>
                <EmailContact>
                  <Address>agent.email@ab.com</Address>
                </EmailContact>
              </Contact>
            </Contacts>
            <OtherIDs>
              <OtherID>00000000</OtherID>
            </OtherIDs>
            <AgencyID>Agency Name</AgencyID>
          </TravelAgencySender>
        </Sender>
      </Party>
      <Query>
        <Order>
          <Offer OfferID="OF-02622d24-9298-4889-9afa-92d5cec9f654" Owner="BA" ResponseID="op08.tx-08-201-f60cf598-ad1a-49f0-bfb1-8e4f85a9fe9b">
            <OfferItem OfferItemID="OF-02622d24-9298-4889-9afa-92d5cec9f654-OI-1">
              <PassengerRefs>SH1</PassengerRefs>
            </OfferItem>
            <OfferItem OfferItemID="OF-02622d24-9298-4889-9afa-92d5cec9f654-OI-2">
              <PassengerRefs>SH2</PassengerRefs>
            </OfferItem>
            <OfferItem OfferItemID="OF-02622d24-9298-4889-9afa-92d5cec9f654-OI-3">
              <PassengerRefs>SH3</PassengerRefs>
            </OfferItem>               
          </Offer>
        </Order>
        <Payments>
          <Payment>
            <Type>CC</Type>
            <Method>
              <PaymentCard>
                <CardType>Credit</CardType>
                <CardCode>VI</CardCode>
                <CardNumber>7777967243366388</CardNumber>
                <SeriesCode>123</SeriesCode>
                <CardHolderName>DR ADULTTHREE SURNAME</CardHolderName>
                <CardHolderBillingAddress>
                  <Street>Test Street1</Street>
                  <Street>Test Street2</Street>
                  <CityName>City</CityName>
                  <PostalCode>AB12CD</PostalCode>
                  <CountryCode>GB</CountryCode>
                </CardHolderBillingAddress>
                <Surcharge>
                  <Amount Code="INR">0</Amount>
                </Surcharge>
                <EffectiveExpireDate>
                  <Expiration>1122</Expiration>
                </EffectiveExpireDate>
              </PaymentCard>
            </Method>
            <Amount Code="INR">20831</Amount>
          </Payment>
        </Payments>
        <DataLists>
          <PassengerList>
            <Passenger PassengerID="SH1">
              <PTC>ADT</PTC>
              <Individual>
                <Birthdate>1986-08-11</Birthdate>
                <Gender>Male</Gender>
                <NameTitle>DR</NameTitle>
                <GivenName>ADULTTHREE</GivenName>
                <Surname>SURNAME</Surname>
              </Individual>
              <IdentityDocument>
                <IdentityDocumentNumber>NI2343243</IdentityDocumentNumber>
                <IdentityDocumentType>709</IdentityDocumentType>
                <IssuingCountryCode>DEU</IssuingCountryCode>
                <CitizenshipCountryCode>DEU</CitizenshipCountryCode>
                <ResidenceCountryCode>DEU</ResidenceCountryCode>
                <ExpiryDate>2027-12-15</ExpiryDate>
                <Birthdate>1986-08-11</Birthdate>
                <Gender>Male</Gender>
              </IdentityDocument>                                    
              <ContactInfoRef>ContactInfo-SH1</ContactInfoRef>                     
              <InfantRef>SH3</InfantRef>
            </Passenger>
            <Passenger PassengerID="SH2">
              <PTC>CHD</PTC>
              <Individual>
                <Birthdate>2012-12-15</Birthdate>
                <Gender>Female</Gender>                     
                <NameTitle>MISS</NameTitle>
                <GivenName>CHILDONE</GivenName>
                <Surname>SURNAME</Surname>
              </Individual>
              <IdentityDocument>
                <IdentityDocumentNumber>NI56152118</IdentityDocumentNumber>
                <IdentityDocumentType>709</IdentityDocumentType>
                <IssuingCountryCode>DEU</IssuingCountryCode>
                <CitizenshipCountryCode>DEU</CitizenshipCountryCode>
                <ResidenceCountryCode>DEU</ResidenceCountryCode>
                <ExpiryDate>2025-12-15</ExpiryDate>
                <Birthdate>2012-12-15</Birthdate>
                <Gender>Female</Gender>
              </IdentityDocument>                     
            </Passenger>
            <Passenger PassengerID="SH3">
              <PTC>INF</PTC>
              <Individual>
                <Birthdate>2020-05-15</Birthdate>
                <Gender>Male</Gender>
                <NameTitle>MSTR</NameTitle>
                <GivenName>INFANTONE</GivenName>
                <Surname>SURNAME</Surname>
              </Individual>
              <IdentityDocument>
                <IdentityDocumentNumber>NI8961529</IdentityDocumentNumber>
                <IdentityDocumentType>709</IdentityDocumentType>
                <IssuingCountryCode>DEU</IssuingCountryCode>
                <CitizenshipCountryCode>DEU</CitizenshipCountryCode>
                <ResidenceCountryCode>DEU</ResidenceCountryCode>
                <ExpiryDate>2023-12-15</ExpiryDate>
                <Birthdate>2020-05-15</Birthdate>
                <Gender>Male</Gender>
              </IdentityDocument>                       
            </Passenger>
          </PassengerList>
          <ContactList>
            <ContactInformation ContactID="ContactInfo-SH1">
              <ContactType>Payment</ContactType>
              <ContactProvided>
                <EmailAddress>
                  <EmailAddressValue>contact.email@ba.com</EmailAddressValue>
                </EmailAddress>
              </ContactProvided>
              <ContactProvided>
                <Phone>
                  <Label>mobile</Label>
                  <CountryDialingCode>44</CountryDialingCode>
                  <AreaCode>44</AreaCode>
                  <PhoneNumber>7000000000</PhoneNumber>
                </Phone>
              </ContactProvided>
            </ContactInformation>
          </ContactList>
        </DataLists>
      </Query>
    </OrderCreateRQ>
