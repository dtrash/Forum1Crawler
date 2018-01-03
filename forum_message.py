import settings


class ForumMessage:

    def __init__(self, *args, parser):
        self.category = args[0]

        scores = parser.parse_score(args[1])
        self.total_score = scores['total_score']
        self.pros_score = scores['pros_score']
        self.cons_score = scores['cons_score']

        user_info = parser.parse_user_info(args[2])
        self.username = user_info['username']
        self.company = user_info['company']

        self.datetime = args[3]
        self.message_id = args[4]
        self.text = args[5]

        self.url = settings.base_url() + self.message_id

    def message_representation(self, message_type):
        if message_type == 'untagged':
            fieldnames = ForumMessage.fieldnames_untagged_message()
        else:
            fieldnames = ForumMessage.fieldnames_pros_or_cons_message()

        result = dict()
        for fieldname in fieldnames:
            result[fieldname] = self.__getattribute__(fieldname)

        return result

    @staticmethod
    def fieldnames_pros_or_cons_message():
        return ['datetime', 'category', 'total_score', 'pros_score', 'cons_score', 'url', 'username', 'company', 'text']

    @staticmethod
    def fieldnames_untagged_message():
        return ['datetime', 'category', 'url', 'username', 'company', 'text']
