package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A type of user that interacts with the system based on an associated role.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemUser  {

  private String uuid;
  private String title;
  private String short-name;
  private String description;
  private List<String> role-ids;
  private List<AuthorizedPrivilege> authorized-privileges;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}