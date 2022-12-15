#Michael Flavin
#Advanced Python Programming
#Final Project



import streamlit as st
import requests
import json


# API request for August time period
def august_time():
    request = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate=2022-08-01T22:59:59.999&pubEndDate=2022-08-02T23:59:59.999')
    # parse json
    x = json.loads(request.text)
    # display 5 vulnerabilities, each with the details below
    for y in range(5):
        st.subheader("----------------------------------------------------------------------------------------------------")
        st.subheader("CVE ID: " + x["vulnerabilities"][0]["cve"]["id"])
        st.subheader("Source Identifier: " + x["vulnerabilities"][0]["cve"]["sourceIdentifier"])
        st.subheader("Published Date: " + x["vulnerabilities"][0]["cve"]["published"])
        st.subheader("Last Modified Date: " + x["vulnerabilities"][0]["cve"]["lastModified"])
        st.subheader("Vulnerability Status: " + x["vulnerabilities"][0]["cve"]["vulnStatus"])
        st.subheader("Vulnerability Description: " + x["vulnerabilities"][0]["cve"]["descriptions"][0]["value"])
        st.subheader("CVSS Version: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["version"])
        st.subheader("Attack Vector: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["attackVector"])
        st.subheader("Attack Complexity: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["attackComplexity"])
        st.subheader("Privileges Required: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["privilegesRequired"])
        st.subheader("User Interaction Requirement: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["userInteraction"])
        st.subheader("Impact of Confidentiality: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["confidentialityImpact"])
        st.subheader("Impact of Integrity: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["integrityImpact"])
        st.subheader("Impact of Availability: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["availabilityImpact"])
        st.subheader("Vulnerability Base Score: " + str(x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseScore"]))
        st.subheader("Vulnerability Base Severity: " + str(x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]))
        st.subheader("----------------------------------------------------------------------------------------------------")

        y += 1

# API request for September time period
def september_time():
    request = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate=2022-09-01T22:59:59.999&pubEndDate=2022-09-02T23:59:59.999')
    # parse json
    x = json.loads(request.text)
    # display 5 vulnerabilities, each with the details below
    for y in range(5):
        st.subheader("----------------------------------------------------------------------------------------------------")
        st.subheader("CVE ID: " + x["vulnerabilities"][0]["cve"]["id"])
        st.subheader("Source Identifier: " + x["vulnerabilities"][0]["cve"]["sourceIdentifier"])
        st.subheader("Published Date: " + x["vulnerabilities"][0]["cve"]["published"])
        st.subheader("Last Modified Date: " + x["vulnerabilities"][0]["cve"]["lastModified"])
        st.subheader("Vulnerability Status: " + x["vulnerabilities"][0]["cve"]["vulnStatus"])
        st.subheader("Vulnerability Description: " + x["vulnerabilities"][0]["cve"]["descriptions"][0]["value"])
        st.subheader("CVSS Version: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["version"])
        st.subheader("Attack Vector: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["attackVector"])
        st.subheader("Attack Complexity: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["attackComplexity"])
        st.subheader("Privileges Required: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["privilegesRequired"])
        st.subheader("User Interaction Requirement: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["userInteraction"])
        st.subheader("Impact of Confidentiality: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["confidentialityImpact"])
        st.subheader("Impact of Integrity: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["integrityImpact"])
        st.subheader("Impact of Availability: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["availabilityImpact"])
        st.subheader("Vulnerability Base Score: " + str(x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseScore"]))
        st.subheader("Vulnerability Base Severity: " + str(x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]))
        st.subheader("----------------------------------------------------------------------------------------------------")

        y += 1

# API request for October time period
def october_time():
    request = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate=2022-10-01T22:59:59.999&pubEndDate=2022-10-02T23:59:59.999')
    # parse json
    x = json.loads(request.text)
    # display 5 vulnerabilities, each with the details below
    for y in range(5):
        st.subheader("----------------------------------------------------------------------------------------------------")
        st.subheader("CVE ID: " + x["vulnerabilities"][0]["cve"]["id"])
        st.subheader("Source Identifier: " + x["vulnerabilities"][0]["cve"]["sourceIdentifier"])
        st.subheader("Published Date: " + x["vulnerabilities"][0]["cve"]["published"])
        st.subheader("Last Modified Date: " + x["vulnerabilities"][0]["cve"]["lastModified"])
        st.subheader("Vulnerability Status: " + x["vulnerabilities"][0]["cve"]["vulnStatus"])
        st.subheader("Vulnerability Description: " + x["vulnerabilities"][0]["cve"]["descriptions"][0]["value"])
        st.subheader("CVSS Version: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["version"])
        st.subheader("Attack Vector: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["attackVector"])
        st.subheader("Attack Complexity: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["attackComplexity"])
        st.subheader("Privileges Required: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["privilegesRequired"])
        st.subheader("User Interaction Requirement: " +x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["userInteraction"])
        st.subheader("Impact of Confidentiality: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["confidentialityImpact"])
        st.subheader("Impact of Integrity: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["integrityImpact"])
        st.subheader("Impact of Availability: " + x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["availabilityImpact"])
        st.subheader("Vulnerability Base Score: " + str(x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseScore"]))
        st.subheader("Vulnerability Base Severity: " + str(x["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]))
        st.subheader("----------------------------------------------------------------------------------------------------")

        y += 1






st.title("Vulnerability Lookup")

st.subheader("USAGE: Enter a 1, 2, or 3 to view published NVD vulnerabilities during the selected time period.")

st.subheader("1 = Between August 1st and August 2nd 2022")
st.subheader("2 = Between September 1st and September 2nd 2022")
st.subheader("3 = Between October 1st and October 2nd 2022")


time = st.text_input("Enter a 1, 2, or 3", "")

# Upon pressing the submit button, the chosen option will execute its corresponding function
# If the option does not match 1, 2, or 3, then a final else msg will be displayed, prompting for a 1, 2, or 3

if (st.button('Submit')):
    result = time.title()
    st.success(result)

    if (time == "1"):
        august_time()

    elif (time == "2"):
        september_time()

    elif (time == "3"):
        october_time()

    else:
        st.subheader("Please enter a 1, 2, or 3.")
