from enum import Enum


class URIComplement(Enum):
    POST_GET_TOKEN = "rest/default/V1/integration/admin/token"
    POST_CUSTOMER = "rest/default/V1/customers"

    GET_CUSTOMER_GROUP_BY_DEFAULT = "rest/default/V1/customerGroups/default"
    GET_CUSTOMER_GROUP_BY_STORE_ID = "rest/default/V1/customerGroups/default/{store_id}"
    GET_SEARCH_CUSTOMER_GROUP = "rest/default/V1/customerGroups/search"
    SEARCH_CRITERIA_PARAMETER_FIELD = "searchCriteria[filterGroups][0][filters][0][field]"
    SEARCH_CRITERIA_PARAMETER_VALUE = "searchCriteria[filterGroups][0][filters][0][value]"
    SEARCH_CRITERIA_PARAMETER_CONDITION = "searchCriteria[filterGroups][0][filters][0][condition_type]"
    SEARCH_CRITERIA_PARAMETER_CURRENT_PAGE = "searchCriteria[currentPage]={current_page}"
    SEARCH_CRITERIA_PARAMETER_PAGE_SIZE = "searchCriteria[pageSize]={page_size}"
    GET_CUSTOMER_GROUP_BY_ID = "rest/default/V1/customerGroups/{group_id}"
    GET_CHECK_DELETION_CUSTOMER_GROUP = "rest/default/V1/customerGroups/{group_id}/permissions"

    DELETE_CUSTOMER_GROUP = "rest/default/V1/customerGroups/{group_id}"

    STORE_ID_KEY_NAME = "{store_id}"
    GROUP_ID_KEY_NAME = "{group_id}"
    PAGE_SIZE_KEY_NAME = "{page_size}"
    CURRENT_PAGE_KEY_NAME = "{current_page}"
