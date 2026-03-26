package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Used to indicate who created a log entry in what role.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LoggedBy  {

  private String party-uuid;
  private String role-id;
  private String remarks;

}