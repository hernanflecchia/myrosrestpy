from attr import dataclass

@dataclass
class PPPActive:
    id: str
    address: str
    caller_id: str
    encoding: str
    limit_bytes_in: str
    limit_bytes_out: str
    name: str
    radius: str
    service: str
    session_id: str
    uptime: str

    def __str__(self) -> str:
        return self.name
        