package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  The actor that produces an observation, a finding, or a risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OriginActor  {

  private String type;
  private String actor-uuid;
  private String role-id;
  private List<Property> props;
  private List<Link> links;

}