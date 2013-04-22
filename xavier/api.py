from tastypie.api import Api

from accounts.api import StudentResource
from attendances.api import AttendanceBookResource, AttendanceResource


v1_api = Api(api_name='v1')
resources = [
    StudentResource,
    AttendanceBookResource, AttendanceResource,
]

# for resource in resources:
#     v1_api.register(resource)
