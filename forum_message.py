
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

        self.id = self.message_id
        self.url = args[6]

        self.usefull_message = args[7]

    @staticmethod
    def message_fieldnames():
        return ['pros_score', 'cons_score', 'total_score', 'usefull_message', 'datetime', 'category', 'id', 'url',
                'username', 'company', 'text']

    def message_representation(self):
        fieldnames = ForumMessage.message_fieldnames()

        result = dict()
        for fieldname in fieldnames:
            result[fieldname] = self.__getattribute__(fieldname)

        return result
