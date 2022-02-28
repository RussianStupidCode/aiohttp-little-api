ADVT_SCHEMA = {
    "type": "object",
    "properties": {
        "owner_id": {
            "type": "integer"
        },

        "title": {
            "type": "string"
        },

        "text": {
            "type": "string"
        },
    }
}

ADVT_CREATE = {
    **ADVT_SCHEMA,
    "required": ["title", "text"]
}

ADVT_UPDATE = {
    **ADVT_SCHEMA,
}