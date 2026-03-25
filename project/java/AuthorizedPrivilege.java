package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuthorizedPrivilege  {

  private String title;
  private String description;
  private List<String> functions-performed;

}