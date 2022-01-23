def get_db_uri(db_cfg: dict) -> str:
    """Builds SQLAlchemy URI

    Parameters
    ----------
    db_cfg : dict
        Database credentials (Postgres/MySQL).
        It has the following keys:
            - dialect
            - driver
            - username
            - password
            - host
            - port
            - database

    Returns
    -------
    db_uri : str
        Connection string of SqlAlchemy

    """
    db_uri = f"{db_cfg['dialect']}+{db_cfg['driver']}://{db_cfg['username']}:{db_cfg['password']}@{db_cfg['host']}:{db_cfg['port']}/{db_cfg['database']}"  # noqa: E501
    return db_uri
