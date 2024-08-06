### MCC

#### Xerox Feed file
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

#### Integration and Events
1. Source type is MCC.
2. Integration batch id is used to find the events.
3. For every file batch id is unique.

#### 
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
4. 
