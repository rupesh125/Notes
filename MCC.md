### MCC

#### 1. Xerox Feed file
1. Increment header counts.
2. Bill index is unique for D records and claims.
3. D and P records have same bill index.
4. For Xerox bill index starts with X for others Genexe, Bunch it starts with other later.
5. There are 3 vendors Xerox, Bunch, Genex.
6. After bill index in D records IRS no is present.
7. Update the claim Number.
8. MBR is only for WC claim and Med line
9. Trailer cound = total - (header+ trailer).
10. SYN are medical details and file also has ICD codes.
11. 1 bill index is 1 D record.
12. For NY surcharges, 1 bill index creates 2 record of payment in the claim.

#### 2. Integration and Events
1. Source type is MCC.
2. Integration batch id is used to find the events.
3. For every file batch id is unique.

#### 3. Claim and DB
1. After event is processed, data will be inserted in claim inj dmg table.
2. MBR payment with different status will be present on the UI.
3. bill index status are as below
   - In -> Auto suspended.
   - CM -> Commited.
   - CL -> Stuck in compliance.
   - FD -> Full Duplicated.
   - HL -> Manually suspended.
   - IA -> Deleted.
   - ER -> Errored out.
4. BREC -> It will update once fee is processed on the MBR payment.
5. Max 5 suspension reason will display.
6. There are 80-85 suspension reasons.
7. Emdeon indicator E is used to print checks
8. In file for evry P records there are that many rows.
9. There is fee review section at the end, processed fee file details are displayed there.
10. For 1 NY surcharges payment, there are 2 entries.
11. There is issue on the lower environment, because of that payee name for NY payment is incorrect and checkbox is not disabled.
12. NY payment can not be posted from the UI, hard edit will appear on payment post.
13. If original payment is posted, NY payment will post automatically.
14. There will be only one entry for NY and original payment in INJ DMG table also G_PYMNT_NY is for NY payment id.

#### 4. TX Activity Outbound
1. Once MBR payment is posted, outbound transaction will be generated for the MBR and payment post.
2. Reports can be triggered after this stage.

#### 5. MBR Reports

##### 1. Emdeon
1. Its location is downstreamfinancial -> checkprint -> emdeon
2. MBR payment that has Emdeon as E will appear in the outbound file.
3. Exceptions are NY payment, EFT, 0 amount payment.

##### 2. Applied Payment Feed
1. Location is MCC -> Applied payment feed.
2. All the posted payments will appear here.

##### 3. Accepted Rejected Report
1. All the accepted, rejected, hold payments will appear here.

##### 4. Medical Data Call
1. GRA -> All MBR payments of contract claims
2. CA/MA/NJ/PA -> All policy payments with respective jurisdictions.
3. CA/MA/NJ/PA/NCCI legacy -> Payments with specific carrier codes.
4. NCCI -> Atlas policy claims with other jurisdictions.
