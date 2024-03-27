from utils import read_file
class JsonHandler:
    """
    This class is for validation JSON files in format AWS::IAM::Role Policy. It checks content of the file according
    to given requirements.
    """
    def __init__(self, filename: str):
        """
        Initializes the file to be loaded.

        :param: str filename: input file
        """
        self.loaded_json = read_file(filename)

    def is_asterisk_resource(self) -> bool:
        """
        Method checks if Resource value in JSON file includes single '*'.
        It checks cases where the is no Resource, when it includes list or a single string.

        :returns: False if Resource contains single '*', else True.
        :rtype: bool
        """
        for statement in self.loaded_json["PolicyDocument"]["Statement"]:
            resource_value = statement.get("Resource")
            # empty case
            if not resource_value:
                continue

            # list case
            elif isinstance(resource_value, list):
                for resource in resource_value:
                    if "*" == resource:
                        return False

            # str case
            elif '*' == resource_value:
                return False
        return True


if __name__ == "__main__":
    iam_handler = JsonHandler("JSON.json")
    print(iam_handler.is_asterisk_resource())
