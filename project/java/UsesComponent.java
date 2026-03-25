package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  The set of components that are used by the assessment platform.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UsesComponent  {

  private String component-uuid;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;

}