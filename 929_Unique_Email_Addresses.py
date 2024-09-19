class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for e in emails:
            local_name, domain_name = e.split("@")
            local_name = local_name.replace(".", "")
            local_name = local_name.split("+")[0]
            unique_emails.add((local_name,domain_name))
        return len(unique_emails)
        