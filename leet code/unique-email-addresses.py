###unique-email-addresses
"""Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

 

Note:

    1 <= emails[i].length <= 100
    1 <= emails.length <= 100
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.

Accepted
143,991
Submissions
208,472"""

def numUniqueEmails(emails):
        eset= set()
        
        for email in emails:
            elist=[]
            for cntr in range(len(email)):
                #print(cntr, end='')
                if email[cntr] == '.':
                    continue
                elif email[cntr] == '+':
                    for i in range(cntr+1, len(email)):
                        if email[i] == '@':
                            elist.append(email[i:])
                            break
                    break
                elif email[cntr]== '@':
                    elist.append(email[cntr:])
                    break
                else:
                    elist.append(email[cntr])
                    #continue
                print(elist)
            em = ''.join(elist)
            eset.add(em)
            print(em)
        return len(eset)


lists=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(lists))