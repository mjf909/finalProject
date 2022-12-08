import streamlit as st
import requests
import json



st.title("Vulnerability Lookup")


st.subheader("USAGE: Simply enter a keyword such as \"Microsoft\" or \"Debian\" to view vulnerabilities regarding your search. ")



name = st.text_input("Enter a keyword", "")

if(st.button('Submit')):
    result = name.title()
    st.success(result)



request = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate=2022-11-01T22:59:59.999&pubEndDate=2022-11-01T23:59:59.999')


# parse x:
x = json.loads(request.text)

st.subheader("-----------------------------------------------------")

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

st.subheader("-----------------------------------------------------")


